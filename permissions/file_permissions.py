



#this is dictionary with permissions about dir.
#first one is for read 
#second for write
#0 => not allowed
#1 => allowed

dir_per = {
    '/',
    '/assets',
    '/proxy',
    '/samplefortemp'
}

prox = ['./documentroot/proxy/proxyfile.html']

proxy_user = ['ram:123']

temporary = {'./documentroot/temp.html':'samplefortemp/temp.html'}

permanent = {'./documentroot/perm.html':'samplefortemp/perm.html'}

authorized = ['./documentroot/auth_file.html']

auth_pass = ['mohit:123']

file_per = {
    'auth_file.html',
    'dashboard.html',
    'favicon.icon',
    'form.html',
    'index.html',
    'menu.html',
    'new-user.html',
    'orders.html',
    'purchases.html',
    'staff.html',
    'suppliers.html',
    'transactions.html',
    '/samplefortemp/perm.html',
    '/samplefortemp/temp.html',
    '/proxy/proxyfile.html'
}   


