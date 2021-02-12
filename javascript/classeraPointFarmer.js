function farm(){
document.getElementsByClassName('add-post-btn')[0].click()

var area = document.getElementById('cke_1_contents').children[1].contentDocument.getElementsByTagName('p')[0]
var message = document.createTextNode('Thanks for your efforts mister')

area.appendChild(message)

document.getElementById('PostReplyForm').children[6].click()
}

x = parseInt(prompt('how many points do you wanna get?'))
if (x % 5 !== 0) { x -= x % 5 }

for (var i = 0; i < x / 5; i++){
	farm()
}
