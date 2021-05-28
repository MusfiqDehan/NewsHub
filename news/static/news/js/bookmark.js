var updateBtns = document.getElementsByClassName('update-bookmark');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var itemId = this.dataset.item;
        var action = this.dataset.action;

        console.log('itemId: ', itemId, 'action: ', action);

        console.log('USER: ', user);

        if (user == 'AnonymousUser') {
            console.log("Not Logged In");
        }
        else {
            updateUserBookmark(itemId, action);
        }

    });
}

function updateUserBookmark(itemId, action) {
    console.log("User is logged in. Sending data...");

    var url = '/update_bookmark/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'itemId': itemId, 'action': action})
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{
        console.log('data:', data);
    })
}