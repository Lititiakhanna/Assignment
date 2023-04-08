from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Blog, Account, Comment
from django.db.models import Q



class AccountView(viewsets.ViewSet):

    def create(self,request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            Account.objects.create(email=email, name=name)

            return Response({"message":"User created successfully", "success": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message":"User not created", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self,request):
        try:
            account_id= request.GET.get('id')
            level = request.GET.get('level')
            account= Account.objects.get(id=account_id)
        
            account_list=set()
            blog_list=set()
            account_list.add(account)
            data=set()
            data.add(account)
            response_data={}

            for obj in range(0,int(level)):
                print(data)
                for user in data:
                    account= Account.objects.get(id=user.id)
                    comment=Comment.objects.filter(account=account) 
                    data=set()
                    for i in comment:
                        users=Comment.objects.filter(blog=i.blog).exclude(Q(account__in=account_list) | Q(blog__in=blog_list))
                        blog_list.add(i.blog)
                        for j in users:
                            data.add(j.account)
                            account_list.add(j.account)
            for i in data:
                response_data[i.id]=i.name

            return Response({"data":response_data, "success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Something went wrong", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retrieve(self,request,pk):
        try:
            account= Account.objects.get(id=pk)
            data={
                "id":account.id,
                "name":account.name,
                "email":account.email
            }
            return Response({"data":data, "success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Data not found", "success": False}, status=status.HTTP_404_NOT_FOUND)
  

class BlogView(viewsets.ViewSet):

    def update(self,request,pk):
        try:
            blog_text = request.data.get('blog_text')
            account = Account.objects.get(id=pk)
            Blog.objects.create(blog_text=blog_text, account=account)

            return Response({"message":"Blog created successfully", "success": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message":"Blog not created", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self,request,pk):
        try:
            blog= Blog.objects.get(id=pk)
            data={
                "id":blog.id,
                "blog_text":blog.blog_text
            }
            return Response({"data":data, "success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Data not found", "success": False}, status=status.HTTP_404_NOT_FOUND)
    

  

class CommentView(viewsets.ViewSet):

    def update(self,request,pk):
        try:
            blog_id=request.GET.get("bid")
            comment = request.data.get('comment')
            account=Account.objects.get(id=pk)
            blog=Blog.objects.get(id=blog_id)
            Comment.objects.create(account=account, comment=comment,blog=blog)

            return Response({"message":"Comment added successfully", "success": True}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message":"Comment not added, try again", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retrieve(self,request,pk):
        try:
            comment= Comment.objects.get(id=pk)
            data={
                "id":comment.id,
                "comment":comment.comment
            }
            return Response({"data":data, "success": True}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Data not found", "success": False}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
