from django.contrib import admin

# Register your models here.
#
 # class AlbumAdmin(admin.ModelAdmin):
 #     list_display = ('title', 'artist', 'price')
 #     list_filter = ('artist',)
 #     search_fields = ('title', 'artist')
 #     def cover_preview (self,obj):
 #         if obj.cover:
 #             return f'<img src="{obj.cover.url}" width="50" height="50" />'
 #         return "No Image"
 #         cover_preview.allow_tags = True
 #         cover_preview.short_description = "Ảnh bìa"
 #
 # class SongAdmin(admin.ModelAdmin):
 #     list_display = ('title', 'album', 'price', 'hien_thi', 'ngay_cap_nhat')  # khớp với model Song
 #     list_filter = ('album', 'hien_thi')
 #     search_fields = ('title',)
 #
 # admin.site.register(Album, AlbumAdmin)
 # admin.site.register(Song, SongAdmin)
