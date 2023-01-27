var date = new Date()
lastDayDate = new Date(date.getFullYear(), date.getMonth() + 1, 0).toLocaleDateString()
lastDay = lastDayDate.toString().match(/^\d+/)[0]

let current_month = date.getMonth()
let current_day = date.toString().match(/\d\d/)[0]
let current_year = date.getFullYear()

const week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

const on_notice = {
    "Mathaus": [6, 7, 8, 9, 10, 11, 12, 13],
    "Fagner": [13, 14, 15, 16, 17, 18, 19, 20],
    "Rafael": [1,2, 3, 4, 5, 20, 21, 22, 23, 24, 25, 26, 27],
    "Darlan": [27, 28, 29, 30, 31]
}

const tag_date = document.querySelector('.date-weekdays')

const ul_weekdays = document.querySelector('.week-days-list')
week_days.map((item) => {
    let tag_li = document.createElement('li')
    let text_li = document.createTextNode(item.toString())
    tag_li.appendChild(text_li)
    ul_weekdays.appendChild(tag_li)
})

const tag_span = document.createElement('span')
const text_span = document.createTextNode(`${month[current_month]}, ${current_year}`)
tag_span.appendChild(text_span)


const tag_arrow_right = document.createElement('i')
const text_arrow_right = document.createTextNode('chevron_right')
tag_arrow_right.appendChild(text_arrow_right)
tag_arrow_right.classList.add('material-icons')

const tag_arrow_left = document.createElement('i')
const text_arrow_left = document.createTextNode('chevron_left')
tag_arrow_left.appendChild(text_arrow_left)
tag_arrow_left.classList.add('material-icons')

const tag_div_btn_date = document.createElement('div')
tag_div_btn_date.appendChild(tag_arrow_left)
tag_div_btn_date.appendChild(tag_span)
tag_div_btn_date.appendChild(tag_arrow_right)

//tag_arrow_left.addEventListener('click', e => alert("ok"))

tag_date.appendChild(tag_div_btn_date)

const list_monthdays = document.querySelector('.month-days-list')
for (let i = 1; i <= parseInt(lastDay); i++) {
    let tag_li = document.createElement('li')
    let text_li = document.createTextNode(i.toString())
    tag_li.appendChild(text_li)
    list_monthdays.appendChild(tag_li)

    if(on_notice["Mathaus"].includes(i)){
        tag_li.classList.add('on-notice-a')
    }
    
    if(on_notice["Fagner"].includes(i)){
        tag_li.classList.add('on-notice-b')
    }
    
    if(on_notice["Rafael"].includes(i)){
        tag_li.classList.add('on-notice-c')
    }
    
    if(on_notice["Darlan"].includes(i)){
        tag_li.classList.add('on-notice-d')
    }

    
    if (i == current_day){
        tag_li.classList.add('current-date-active')
    }
}