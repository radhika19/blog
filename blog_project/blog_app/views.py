"views for Blog"
import json
from rest_framework import status
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog_app.models import Blog, Paragraph, Comment
from blog_app.serializer import BlogSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
def blogs_list(request):
    "GET: displays all the blogs POST: take a new blog as I/P (or) modified text"
    if request.method == 'GET':
        blogs = Blog.objects.all()
        pages = PageNumberPagination()
        page_data = pages.paginate_queryset(blogs, request)
        serializer = BlogSerializer(page_data, many=True)
        return pages.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        title = data.pop('title')
        text = data.pop('text')
        try:
            blog_exists = Blog.objects.filter(title=title)
            if blog_exists:
                para_list = text.split('\n\n')
                para_text = Paragraph.objects.filter(blog=blog_exists)
                dummy = json.loads(blog_exists[0].seq)
                para_delete = para_text.exclude(text__in = para_list)
                if para_delete:
                    comm_delete = Comment.objects.filter(paragraph__in=para_delete).delete()
                    for i in para_delete:
                        dummy.remove(i.id)
                    para_delete.delete()
                para_text = para_text.filter().values_list('text', flat=True)
                for i in range(0, len(para_list)):
                    if para_list[i] not in para_text:
                        para_save = Paragraph(blog=blog_exists[0], text=para_list[i])
                        para_save.save()
                        dummy = dummy[:i] + [para_save.id] + dummy[i:]
                blog_exists[0].seq = json.dumps(dummy)
                blog_exists[0].save()
                return Response({"status":"success", "message":"Text is updated"}, status=status.HTTP_201_CREATED)
            else:
                blog_save = Blog(title=title)
                blog_save.save()
                paragraphs = text.split('\n\n')
                para_list = [Paragraph(blog=blog_save, text=t) for t in paragraphs]
                Paragraph.objects.bulk_create(para_list)
                if para_list:
                    blog_save.seq = json.dumps(list(Paragraph.objects.filter(blog=blog_save).order_by('id').values_list('id', flat=True)), cls=DjangoJSONEncoder)
                else:
                    blog_save.seq = json.dumps(list())
                blog_save.save()
                return Response({"status":"success", "message":"New Blog created"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"status":"fail", 'message':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def blog_list(request, pk):
    "GET: display the paragraph and comments of a specific Blog POST:store comments for that blog"
    if request.method == 'GET':
        try:
            response = {}
            blog = Blog.objects.get(id=pk)
            response['blog_id'] = blog.id
            response['blog_title'] = blog.title
            sequence = json.loads(blog.seq)
            response['paragraphs'] = []
            for para_id in sequence:
                paragraph = {}
                para = Paragraph.objects.get(id=para_id)
                comments = Comment.objects.filter(paragraph=para_id).values('id', 'comment')
                paragraph['id'] = para_id
                paragraph['text'] = para.text
                paragraph['comments'] = comments
                response['paragraphs'].append(paragraph)
            return Response(response)
        except Exception as ex:
            return Response({'status':'fail', 'message':str(ex)})
    elif request.method == 'POST':
        try:
            data = request.data
            comments = data.pop('comments')
            comments_dict = {}
            for comment in comments:
                comments_dict.update({int(comment.keys()[0]):comment.values()[0]})
            blog_id = data.pop('blog_id')
            comm_para = Comment.objects.filter(paragraph__blog__in=Blog.objects.filter(id=blog_id))
            comm_delete = list(set(dict(comm_para.values_list('paragraph__id', 'comment')).items()) - set(comments_dict.items()))
            comm_add = list(set(comments_dict.items())-set(dict(comm_para.values_list('paragraph__id', 'comment')).items()))            
            for comment in comm_delete:
                comm_para.filter(paragraph_id=comment[0], comment=comment[1]).delete()
            for comment in comm_add:
                com_save = Comment(paragraph_id=int(comment[0]), comment=comment[1])
                com_save.save()
            return Response({"status":"success", "message":"Comment successfully updated"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"status":"fail",'message':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
