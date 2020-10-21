



#this is dictionary with permissions about dir.
#first one is for read 
#second for write
#0 => not allowed
#1 => allowed

dir_per = {
    '/' : [1,1],
    '/css' : [1,0],
    '/images' : [1,0],
    '/dir1' : [1,1],
    '/dir2' : [1,1],
    '/permissions':[0,0],
    '/server_data':[0,0]
}



file_per = {
    "/dir1/hello.txt":[1,1],
    '/hel.txt':[1,1],
    "/404.css" : [1,0],
    "/404.html" : [1,0],
    "/about.html" : [1,0],
    "/blog.html" : [1,0],
    "/cakewebsitetemplate.psd" : [1,0],
    "/contact.html" : [1,0],
    "/favicon.ico":[1,0],
    "/form.html":[1,0],
    "/index.html":[1,0],
    "/product.html":[1,0],
    "/signin.html":[1,0],
    "/signup.html":[1,0],
    "/services.html":[1,0],
    "/css/ie6.css":[1,0],
    "/css/ie7.css":[1,0],
    "/css/ie8.css":[1,0],
    "/css/style.css":[1,0],
    "/images/arrow-down.gif":[1,0],
    "/images/arrow-up.gif":[1,0],
    "/images/bg-body.gif":[1,0],
    "/images/bg-featured.jpg":[1,0],
    "/images/bg-featured-bottom-curve.jpg":[1,0],
    "/images/bg-featured-heading.gif":[1,0],
    "/images/bg-foodstory-bottom.gif":[1,0],
    "/images/bg-foodstory.gif":[1,0],
    "/images/bg-foodstory-top.gif":[1,0],
    "/images/bg-footer2.gif":[1,0],
    "/images/bg-footer.gif":[1,0],
    "/images/bg-form.gif":[1,0],
    "/images/bg-form-bottom-curve.gif":[1,0],
    "/images/bg-form-top-curve.gif":[1,0],
    "/images/bg-post.gif":[1,0],
    "/images/bg-post-footer.gif":[1,0],
    "/images/bg-post-header.gif":[1,0],
    "/images/bg-readmore.gif":[1,0],
    "/images/bg-sign-up.gif":[1,0],
    "/images/bg-sweets.gif":[1,0],
    "/images/border-horizontal.gif":[1,0],
    "/images/burgercake.jpg":[1,0],
    "/images/cake.jpg":[1,0],
    "/images/cakes.jpg":[1,0],
    "/images/cupcake.jpg":[1,0],
    "/images/dessert.jpg":[1,0],
    "/images/desserts.jpg":[1,0],
    "/images/footer-top-border.jpg":[1,0],
    "/images/fruit-cake.jpg":[1,0],
    "/images/fruit.jpg":[1,0],
    "/images/healthy-food.jpg":[1,0],
    "/images/input-contact.gif":[1,0],
    "/images/input-search.gif":[1,0],
    "/images/italian.jpg":[1,0],
    "/images/logo.gif":[1,0],
    "/images/pasteries.jpg":[1,0],
    "/images/pie.jpg":[1,0],
    "/images/sidebar-separator.gif":[1,0],
    "/images/special-treats.jpg":[1,0],
    "/images/sprite-buttons.gif":[1,0],
    "/images/sprite-icons.gif":[1,0],
    "/images/tarts.jpg":[1,0],
    "/images/wedding-cupcakes-large.jpg":[1,0],
    "/images/wedding-cupcakes-small.jpg":[1,0],
    "/server_data/post_log.txt":[0,0],
    "/permissions/file_permissions.py":[0,0]
}   


