
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from feedsblog import db
from feedsblog.models import Post
from feedsblog.posts.forms import PostForm

posts=Blueprint("posts",__name__)

@posts.route("/post/new",methods=['GET','POST'])
@login_required
def feeds_post():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,body=form.post.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Your Post has been Posted',"success")
        return redirect(url_for("main.home"))

    return render_template("newpost.html",title="New Post",form=form)

@posts.route("/post/<int:post_id>",methods=['GET','POST'])

def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template("singlepost.html",title=post.title,legend="New Post")

@posts.route("/post/<int:post_id>/update",methods=['GET','POST'])

def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    form=PostForm()
    if post.author!=current_user:
        abort(403)
    if form.validate_on_submit():
        post.title=form.title.data
        post.body=form.post.data
        db.session.commit()
        flash(f'Your post has been updated','success')
        return redirect(url_for("posts.post",post_id=post.id))

    elif request.method=="GET":
        form.title.data=post.title
        form.post.data=post.body

    return render_template("newpost.html",form=form,title="update"+post.title,legend="Update Post")

@posts.route("/post/<int:post_id>/delete",methods=['POST'])

def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    form=PostForm()
    if post.author!=current_user:
        abort(403)
    else:
        db.session.delete(post)
        db.session.commit()
        flash(f'Your post has been deleted','success')
        return redirect(url_for("main.home"))
