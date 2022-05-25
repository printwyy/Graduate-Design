"""managesys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from agripro import views
urlpatterns = [
    path('admin/', admin.site.urls),  #owner 123456
    path('',views.insys,name='insys'),
    path('auth-login/',views.login,name='auth-login'), #登录
    path('logout/',views.logout,name='logout'), #登出
    path('auth-register/',views.register,name='auth-register'),#注册
    path('getusername/',views.getusername,name='getusername'),
    path('myself/',views.myself,name='myself'),
    path('seluser/<wid>/',views.seluser,name='seluser'), #调配

    # 决策部分
    path('index/',views.index,name='index'),
    path('usersave/',views.usersave,name='usersave'),
    path('inoutdetail/',views.inoutdetail,name='inoutdetail'),
    path('fbcloud/',views.fbcloud,name='fbcloud'),
    path('blockdetail/',views.blockdetail,name='blockdetail'),
    path('outpredict/',views.outpredict,name='outpredict'),

    #仓库管理模块
    path('storage-index/<identify>/',views.storageindex,name='storage-index'), #仓库首页
    path('storagewarn/<identify>/',views.storagewarn,name='storagewarn'), #库存预警
    path('selwarn/',views.selwarn,name='selwarn'),
    path('storagedetail/<nid>/',views.storagedetail,name='storagedetail'),#库存详情
    path('entryregist/',views.entryregist,name='entryregist'), #入库登记
    path('eanget/',views.eanget,name='eanget'), #前端识别条码并检索函数
    path('goodsave/',views.goodsave,name='goodsave'), #登记入库函数
    path('outstorage/',views.outstorage,name='outstorage'), #出库
    path('outsave/',views.outsave,name='outsave'), #出库保存函数
    path('stordispatch/',views.stordispatch,name='stordispatch'), #调配

    path('financeindex/',views.financeindex,name='financeindex'), #财务首页
    path('income/<identify>/',views.income,name='income'),
    path('outcome/<identify>/',views.outcome,name='outcome'),

    path('dispatchup/',views.dispatchup,name='dispatchup'), #调配
    path('dispatchsave/',views.dispatchsave,name='dispatchsave'),
    path('dispatchdetail/<identify>/',views.dispatchdetail,name='dispatchdetail'), #调配


    #农户模块
    path('farmerindex/',views.farmerindex,name='farmerindex'), #农户首页
    path('fbsave/',views.fbsave,name='fbsave'), #保存意见
    path('farmersel/',views.farmersel,name='farmersel')

]
