
md5pw = "202CB962AC59075B964B07152D234B70";

function checkuser() {
    
    password = faultylabs.MD5($('password'));
    if ($('username') == "test" && password == md5pw) {
        window.location.href = "astData.html?username=" + $('username') + "&" + "password=" + password;
    } else {
        alert("Wrong username or password!")
    }
}

function $(id) {
    return document.getElementById(id).value;
}

function getQueryString() {
    var result = {}, queryString = location.search.slice(1),
        re = /([^&=]+)=([^&]*)/g, m;

    while (m = re.exec(queryString)) {
        result[decodeURIComponent(m[1])] = decodeURIComponent(m[2]);
    }

    return result;
}