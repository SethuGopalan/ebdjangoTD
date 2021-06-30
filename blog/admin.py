from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from  blog.models import Profile,Post,Tag

@admin.register(Profile)
class ProfileAdmin(admin,ModelAdmin):
    model = Profile
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display =(

        "id",
        "title",
        "subtitle",
        "slug",
        "publish_data",
        "published",
    )
    list_filter= (
        "published",
        "publish_data",

    )
    list_editable =(

        "title",
        "subtitle",
        "slug",
        "published_date",
        "published"
    )
    serch_feilds=(
        "title",
        "subtitle",
        "slug",
        "body",

    )
    prepopulated_fields=(

        "slug",
        "title",
        "subtitle",

    )
    date_hierarchy = "publish_date"
    save_on_top = True
