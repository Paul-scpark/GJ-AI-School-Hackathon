from django.shortcuts import render, redirect
from.models import write_post

# Create your views here.
def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def logout(request):
    return redirect('main.html')

def search(request):
    return render(request, 'search.html')

row_per_page = 10

def post(request):
    post_lst = write_post.objects.order_by('-id')[0:10]
    current_page = 1
    total_cnt = write_post.objects.all().count()

    helper = page_helper()
    total_page_lst = helper.getTotalPage_lst(total_cnt, row_per_page)

    context = {
        'post_lst' : post_lst,
        'total_cnt' : total_cnt,
        'current_page' : current_page,
        'total_page_lst' : total_page_lst
    }

    return render(request, 'post.html', context)


class page_helper:
    def __init__(self):
        self.total_pages = 0
        self.total_page_lst = 0
    
    def getTotalPage_lst(self, total_cnt, row_per_page):
        if ((total_cnt % row_per_page == 0)):
            self.total_pages = total_cnt // row_per_page
            print('get total page #1')

        else:
            self.total_pages = (total_cnt // row_per_page) + 1
            print('get total_page #2')

        self.total_page_lst = []
        for j in range(self.total_pages):
            self.total_page_lst.append(j + 1)
    
        return self.total_page_lst



def page(request, post_pk):
    post_object = write_post.objects.get(pk=post_pk)

    context = {
        'post_object' : post_object
    }

    return render(request, 'page.html', context)


area_lst = ['서울특별시', '인천광역시', '경기도', '강원도',
            '충청남도', '세종특별자치시', '대전광역시', '충청북도',
            '경상북도', '경상남도', '대구광역시', '전라북도', 
            '전라남도', '광주광역시', '울산광역시', '부산광역시', '제주특별자치시도']

voluteer_type_lst = ['자연환경보호활동', '지역사회봉사활동', '기술지원', '업무보조', 
                    '정서지원', '기타봉사', '생활지원', '전문봉사']

def write_page(request):

    context = {
        'area_lst' : area_lst,
        'voluteer_type_lst' : voluteer_type_lst,
    }


    if request.method == 'POST':
        write_post.objects.create(
            title = request.POST['title'],
            area = request.POST['area'],
            term = request.POST['term'],
            volunteer_type = request.POST['volunteer_type'],
            how_many = request.POST['how_many'],
            memo1 = request.POST['memo1'],
            memo2 = request.POST['memo2'],
            memo3 = request.POST['memo3'],
            name = request.POST['name'],
            email = request.POST['email'],
            phone_num = request.POST['phone_num'],
            affiliation = request.POST['affiliation']
        )

        return redirect('post')

    return render(request, 'write_page.html', context)