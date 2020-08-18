from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'newsApp/index.html')
def sportsnews(request):
    head_msg='Sports news'
    msg1='No T20 world cup this year'
    msg2='IPL postponed'
    msg3='Paskitan players test positive for covid19'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
def moviesnews(request):
    head_msg='Movies news'
    msg1='SSRs death leave everyone shocked'
    msg2='Theatres to remanin closed till 31st july'
    msg3='Big releases on online streaming platform in july'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
def politicsnews(request):
    head_msg='Poilitics news'
    msg1='Indo-China situation remains escalated'
    msg2='Modi addressed the country yestarday at 4 P.M'
    msg3='Paskistan deploy army near the borders'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
