function clearBlock(block) {
    var block = document.getElementById('paged_block-' + block).children[0].children;

    for (var i = 0; i <= 10; i++){
        var link = block[i].children[1].children[0].getAttribute('href');

        window.open('https://me.classera.com' + link);
    }
}


var x_block = prompt('Which block do you wanna whipe today?');
clearBlock(x_block)
