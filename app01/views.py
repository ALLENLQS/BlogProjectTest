from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

def base(request):
    return render(request, 'app01/base.html')

def index(request):
    return render(request, "app01/index.html")

def myArticle(request):
    return render(request, "app01/myArticle.html")

def myArticle_v1(request):
    return render(request, "app01/myArticle_v1.html")

def myPicture(request):
    return render(request, "app01/myPicture.html")

def aboutMe(request):
    return render(request, "app01/aboutMe.html")

def connectMe(request,name):
    return render(request, "app01/aboutMe.html")

def vuejsExample(request):
    return render(request, 'app01/vuejsExample.html')

from django.http import JsonResponse
from django.views.generic import View
class Api(View):
    def get(self,request):
        return JsonResponse({"method":request.method})
    def post(self,request):
        return JsonResponse({"method":request.method})

from app01.forms import CommentForm,CommentForm_aboutModel
def aboutMe1(request):
    form = CommentForm_aboutModel()
    if request.method == "POST" and request.POST:
        requestData = CommentForm_aboutModel(request.POST)
        if requestData.is_valid():
            clean_data = requestData.cleaned_data
            return JsonResponse({"data":clean_data})
        else:
            return JsonResponse({"data":requestData.errors})
    return render(request,"app01/aboutMe.html",{"form":form})
from app01.models import Article
def example(request):
    all_data = Article.objects.all()
    count = Article.objects.article_count("库克：人工智能要想真正聪明 必须尊重人类的价值观") #调用自定义的查询方法
    return render(request,"app01/example_model.html",locals())


def vuePageData(request):
    if request.method == 'GET':#如果是get请求
        page = request.GET.get('page')#尝试获取page
        if not page:#默认page为1
            page = 1
        else:
            page = int(page)#get过来的page参数是字符串
        article = Article.objects.all()#查询所有的数据
        paginator = Paginator(article,11)#对数据进行分页，每页5条
        pageData = paginator.page(page)#获取具体页的数据
        page_data = []#对数据进行json结构化，json只接受字典对象
        for data in pageData:
            classify = data.classify.name#多对多字段需要首先查询出所有对应的字段，查询出来还是数据库对象
            if classify:
                classify = [i.label for i in classify]#对字段取指定的label
            else:
                classify = ""#空列表不可以创建json序列，所以我们改为字符串
            page_data.append(
                {
                    "title":data.title,
                    "author": data.author.name,#外键必须调用具体的字段
                    "time": data.time,
                    "description": data.description,
                    "picture": data.picture.name,#这里的name是由于文件对象有name属性
                    "classify": classify,
                    "id": data.id,
                 }
            )
        # print(data.classify)
        result = {
            "pageData":page_data
        }
        return JsonResponse(result)

def vuePageData_v1(request):
    selectPage = 3 #每次3页
    pageNum = 3 #每页3条
    totolNum = selectPage * pageNum #单次查询9条
    result_dict = {}

    if request.method == "GET":
        pageNow = request.GET.get("page")
        if pageNow and int(pageNow) > 1:
            pageNow = int(pageNow)
        else:
            pageNow = 1
        # 获取查询序列号
        queryNum = pageNow/pageNum
        if queryNum == int(queryNum):
            queryNum = int(queryNum)
        else:
            queryNum = int(queryNum) + 1

        start = (queryNum -1 ) * totolNum
        end = queryNum * totolNum + 3 #这里为什么要+3
        articles = Article.objects.all()[start:end]
        paginator = Paginator(articles,pageNum)
        pageData = paginator.page(pageNow-start/pageNum)
        page_data = []

        for data in pageData:
            page_data.append(
                {
                    "title": data.title,
                    "author": data.author.name,
                    "time": data.time,
                    "picture": data.picture.name,  # 这里要注意，data.picture 返回的是图片对象，我们获取他的name
                    'description': data.description,
                    'id': data.id,
                }
            )
        result_dict["pageData"] = page_data

        if pageNow % selectPage == 0 and len(paginator.page_range) > 3: #这里为什么这么写
            result_dict["page_range"] = [page + pageNum* (queryNum - 1) for page in paginator.page_range] #这里的逻辑不懂
        else:
            result_dict["page_range"] = [page + pageNum * (queryNum - 1) for page in paginator.page_range][:-1]

        return JsonResponse(result_dict)