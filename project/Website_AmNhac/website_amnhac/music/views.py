from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from django.contrib import messages
from .forms import AlbumForm, SongForm, ArtistForm, RegisterForm, SongFormSet, OrderForm, ContactForm
from .models import Album, Song, Artist, CartItem,Order,OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    featured_artist = Artist.objects.first()
    featured_song = None
    form = ContactForm()
    if featured_artist and featured_artist.albums.exists():
        first_album = featured_artist.albums.first()
        if first_album.songs.exists():
            featured_song = first_album.songs.first()
    albums = Album.objects.all()[:12]
    return render(request, "music/index.html", {
        "featured_artist": featured_artist,
        "featured_song": featured_song,
        "albums": albums,
        "form":form
    })


def albums_store(request):
    """Trang albums với lọc theo chữ cái hoặc số"""
    letter = request.GET.get('letter')

    if letter == '0':  # lọc theo số
        albums = Album.objects.filter(title__regex=r'^[0-9]')
    elif letter:
        albums = Album.objects.filter(title__istartswith=letter)
    else:
        albums = Album.objects.all()

    paginator = Paginator(albums, 6)  # mỗi trang 1 album
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music/albums-store.html', {
        'page_obj': page_obj,   # chỉ cần page_obj
    })

def albums_detail(request, album_id):

    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()  # assuming Song has ForeignKey(Album, related_name='songs')

    return render(request, 'music/albums_detail.html', {
        'album': album,
        'songs': songs
    })

def add_form(request):
    SongFormSet = inlineformset_factory(Album, Song, form=SongForm, extra=1, can_delete=False)

    if request.method == "POST":
        album_form = AlbumForm(request.POST, request.FILES)
        song_formset = SongFormSet(request.POST, request.FILES)
        if album_form.is_valid() and song_formset.is_valid():
            album = album_form.save()
            songs = song_formset.save(commit=False)
            for song in songs:
                song.album = album
                song.save()
            for obj in song_formset.deleted_objects:
                obj.delete()
            return redirect('albums')
    else:
        album_form = AlbumForm()
        song_formset = SongFormSet()

    return render(request, 'music/Album_form.html', {
        'album_form': album_form,
        'song_formset': song_formset,
        'title': "Add new album",
    })

def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('albums')
    else:
        form = ArtistForm()
    return render (request, 'music/add_artist.html', {
        'form':form,
        'title':'Add artist',
    })

def edit_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        formset = SongFormSet(request.POST, request.FILES, instance=album)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("albums_detail", album_id=album.id)
    else:
        form = AlbumForm(instance=album)
        formset = SongFormSet(instance=album)

    return render(request, "music/edit_album.html", {
        "form": form,
        "formset": formset,
        "album": album,
        "title": "Edit Album"
    })

def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == "POST":
        album.delete()
        return redirect("albums")

    return render(request, "music/delete_album.html", {
        "album": album,
        "title": "Delete Album"
    })

def play_first_song(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    first_song = album.songs.first()
    return render(request, 'music/play_first_song.html', {
        'album': album,
        'song': first_song
    })

def events(request):
    return render(request, 'music/events.html')


def blog(request):
    return render(request, 'music/blog.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cam on ban da lien he!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'music/contact.html', {'form': form})

def customer(request):
    customers = User.objects.filter(is_staff=False)  # lọc ra user thường
    return render(request, "music/customer.html", {"customers": customers}) 

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()          # tự động tạo user với password1/password2
            login(request, user)        # đăng nhập ngay sau khi đăng ký
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "music/dangky.html", {
        "form": form,
        "title": "Register"
    })
def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "music/login.html",{
        "form":form,
        "title":"Login"
    })
def logout_views(request):
    """Đăng xuất"""
    logout(request)
    return redirect("home")

def add_to_cart(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.user.is_authenticated:
        # Nếu đã đăng nhập → lưu vào DB
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            album=album,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        # Nếu chưa đăng nhập → lưu vào session
        cart = request.session.get('cart', {})
        cart[str(album_id)] = cart.get(str(album_id), 0) + 1
        request.session['cart'] = cart

    return redirect('albums')

def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price for item in cart_items)
    else:
        cart = request.session.get('cart', {})
        cart_items = []
        total_amount = 0
        for album_id, quantity in cart.items():
            album = get_object_or_404(Album, id=album_id)
            cart_items.append({
                "album": album,
                "quantity": quantity,
                "total_price": album.price * quantity,
            })
            total_amount += album.price * quantity

    return render(request, "music/cart.html", {
        "cart_items": cart_items,
        "total_amount": total_amount,
    })


def remove_from_cart(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.user.is_authenticated:

        CartItem.objects.filter(user=request.user, album=album).delete()
    else:

        cart = request.session.get("cart", {})
        if str(album_id) in cart:
            del cart[str(album_id)]
            request.session["cart"] = cart

    return redirect("cart")


def update_cart(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    quantity = int(request.POST.get("quantity", 1))

    if quantity < 1:
        messages.warning(request, "Số lượng cập nhật không hợp lệ")
        return redirect("cart")

    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=request.user, album=album).first()
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f"Cập nhật {album.title} thành {quantity} sản phẩm.")
        else:
            messages.warning(request, f"{album.title} chưa có trong giỏ hàng.")
    else:
        cart = request.session.get("cart", {})
        if str(album_id) in cart:
            cart[str(album_id)] = quantity
            request.session["cart"] = cart
            messages.success(request, f"Cập nhật {album.title} thành {quantity} sản phẩm.")

    return redirect("cart")


def get_cart_total(request):
    """Hàm tính tổng tiền giỏ hàng hiện tại"""
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price for item in cart_items)
    else:
        cart = request.session.get("cart", {})
        total_amount = 0
        for album_id, quantity in cart.items():
            album = Album.objects.get(id=album_id)
            total_amount += album.price * quantity
    return total_amount

def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # tạo Order từ form
            total = 0

            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        album=item.album,
                        quantity=item.quantity,
                        price=item.album.price
                    )
                    total += item.album.price * item.quantity
                cart_items.delete()
            else:
                cart = request.session.get("cart", {})
                for album_id, quantity in cart.items():
                    album = Album.objects.get(id=album_id)
                    OrderItem.objects.create(
                        order=order,
                        album=album,
                        quantity=quantity,
                        price=album.price
                    )
                    total += album.price * quantity
                request.session["cart"] = {}

            order.total_amount = sum(item.total_price for item in order.items.all())
            order.save()

            return redirect("checkout_success", order_id=order.id)
    else:
        form = OrderForm()

    return render(request, "music/checkout.html", {"form": form})

def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "music/checkout_success.html", {"order": order})
@login_required
def account_view(request):
    return render(request, 'music/account.html', {"user": request.user})

@staff_member_required
def all_orders(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "music/all_orders.html", {"orders": orders})

