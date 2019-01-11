function timedCount() {
    
    postMessage(0);
    setTimeout("timedCount()",1000/6);
}

timedCount();