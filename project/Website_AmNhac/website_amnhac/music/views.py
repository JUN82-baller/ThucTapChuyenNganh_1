from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def home(request):
    """Trang chủ"""
    return render(request, 'music/index.html')


def albums_store(request):
    """Trang albums"""
    return render(request, 'music/albums-store.html')


def events(request):
    return render(request, 'music/events.html')


def blog(request):
    return render(request, 'music/blog.html')


def contact(request):
    return render(request, 'music/contact.html')

def customer(request):
    return render(request, 'music/customer.html')
def login(request):
    """Trang đăng nhập bằng email"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "Tài khoản chưa được kích hoạt, vui lòng kiểm tra email")
            else:
                messages.error(request, "Sai tài khoản hoặc mật khẩu")
        except User.DoesNotExist:
            messages.error(request, "Email không tồn tại")

    return render(request, "music/login.html")


def register_view(request):
    """Trang đăng ký"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại, vui lòng chọn tên khác")
            return render(request, "music/dangky.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng, vui lòng chọn email khác")
            return render(request, "music/dangky.html")

        if password1 != password2:
            messages.error(request, "Mật khẩu xác nhận không khớp")
            return render(request, "music/dangky.html")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_active = False
        user.save()

        subject = "Xác nhận tài khoản One Music"
        message = f"Xin chào {user.username}, vui lòng click vào link sau để kích hoạt tài khoản:\nhttp://127.0.0.1:8000/xacthuc/{user.pk}/"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)

        messages.success(request, "Vui lòng kiểm tra email để xác thực tài khoản")
        return redirect("login")

    return render(request, "music/dangky.html")


def activate_account(request, user_id):
    """Kích hoạt tài khoản qua link email"""
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "Tài khoản đã được kích hoạt, bạn có thể đăng nhập.")
    return redirect("login")


def logout_views(request):
    """Đăng xuất"""
    auth_logout(request)
    return redirect("home")
