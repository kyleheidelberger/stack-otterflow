function q(sel) {
    return document.querySelector(sel)
}


function qs(sel) {
    return document.querySelectorAll(sel)
}

var csrftoken = Cookies.get('csrftoken');
let favButton2 = q('.new_favorite')
let answerButton = q('#answer_form')
let newComment = q('#questionAnswerForm')


favButton2.addEventListener('click', function (e) {
    e.preventDefault();
    console.log('favButton2')
    $.ajax({
        type: 'POST',
        url: $("#new_favorite").attr('action'),
        data: {
            'question': $('.question').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function () {
            alert('Added to favorites!')
        },
    })
})

let addFavorite = q('.favorite')
addFavorite.addEventListener('click', function () {
    if (addFavorite.value === "Add to Favorites") {
        addFavorite.value = "Remove from Favorites";
        addFavorite.innerHTML = "Remove from Favorites";
    }
    else {
        addFavorite.value = "Add to Favorites";
        addFavorite.innerHTML = "Add to Favorites";
    }
})




newComment.addEventListener('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/answer/add/',
        data: {
            'answer': $('.newAnswer').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function (data) {
            $('.commentStyle').append(data)
        }
    });
});

// Best Answer Button

let buttons = qs(".bestAnswerButton")

for (let button of buttons) {
    button.addEventListener('click', function () {
        console.log("tracking this?")
        const checkmarks = qs(".checkmark")
        for (let checkmark of checkmarks) {
            checkmark.innerHTML = "✔"
        }
        console.log(checkmark)
    }
    )
}
