// Sticky
var sticky = document.getElementById("sticky"),
    offset = sticky.getBoundingClientRect().top + window.scrollY,
    width = sticky.offsetWidth;

if (window.innerWidth > 768) {
    window.addEventListener("scroll", function() {
        var scrollPosition = window.scrollY;
        if (scrollPosition > offset) {
            sticky.classList.add("is-sticky");
        } else {
            sticky.classList.remove("is-sticky");
        }
        sticky.style.width = scrollPosition > offset ? width + "px" : "";
    });
}

//Functions
function getSmiley(str) {
    return decodeURIComponent(escape(str));
}

function getTopFive(obj) {
    return Object.keys(obj).sort((a, b) => obj[b] - obj[a]).slice(0, 5);
  }




// Graphs

var data0 = [{
    y: Object.values(JSON.parse(document.querySelector(".list0").textContent)),
    x: Object.keys(JSON.parse(document.querySelector(".list0").textContent)),
    type: 'bar'
}];

var layout0 = {
    showlegend: false
};

Plotly.newPlot('count_msg_per_day', data0, layout0, {scrollZoom: false, responsive: true});


var orderedDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
var l19 = JSON.parse(document.querySelector(".list19").textContent);
var data19 = [{
    y: orderedDays.map(day => l19[day]),
    x: orderedDays,
    type: 'bar'
}];

var layout19 = {
    showlegend: false
};

Plotly.newPlot('count_msg_per_day_of_week', data19, layout19, {scrollZoom: false, responsive: true});



var data21 = [{
    y: [...Array(24).keys()].map(function(x) { return JSON.parse(document.querySelector(".list21").textContent)[x.toString().padStart(2, '0')] }),
    x: [...Array(24).keys()].map(function(x) { return x.toString().padStart(2, '0') + ":00" }),
    type: 'bar'
}];

var layout21 = {
    showlegend: false,
    xaxis:{
        tickangle: -45,
        tickfont: {
            size: 9
        }
    }
};

Plotly.newPlot('count_msg_per_hour_of_day', data21, layout21, {scrollZoom: false, responsive: true});




var data1 = [{
    values: Object.values(JSON.parse(document.querySelector(".list1").textContent)),
    labels: Object.keys(JSON.parse(document.querySelector(".list1").textContent)),
    type: 'pie'
}];

var layout1 = {
    showlegend: true
};

Plotly.newPlot('msg_number_participants', data1, layout1, {scrollZoom: false, responsive: true});




max_content = JSON.parse(document.querySelector(".list2").textContent)
document.querySelector(".list2").innerHTML =
`<div class='text-bubble'>${max_content['Message']}</div>
<div class="text-end author"><strong>Author: ${max_content['Author']}</strong>
<sup>Length: ${max_content['Length']}</sup></div>`;





l3 = JSON.parse(document.querySelector(".list3").textContent)

var data3 = [];

for (var year in l3) {
    var tabX3 = Object.keys(l3[year]);
    var tabY3 = Object.values(l3[year]);

    data3.push({
        x: tabX3,
        y: tabY3,
        name: year,
        type: 'bar'
    });
}


var layout3 = {
    showlegend: true
};

Plotly.newPlot('frequency_msg_per_user_per_year', data3, layout3, {scrollZoom: false, responsive: true});

var l18 = JSON.parse(document.querySelector(".list18").textContent);
var data18 = [];
for (var year in l18) {
    var tabX18 = Object.keys(l18[year]);
    var tabY18 = Object.values(l18[year]);

    data18.push({
        x: tabX18,
        y: tabY18,
        name: year,
        type: 'bar'
    });
}


var layout18 = {
    showlegend: true,
    scattergap: 0.3
};

Plotly.newPlot('count_unsent_msg_per_user_per_month', data18, layout18, {scrollZoom: false, responsive: true});



var list4 = JSON.parse(document.querySelector(".list4").textContent);
for (var key in list4) {
    list4[getSmiley(key)] = list4[key];
    delete list4[key];
}
document.querySelector(".list4").innerHTML =JSON.stringify(list4);

var data4 = [{
    y: Object.values(list4).sort((a, b) => b - a).slice(0, 10),
    x: Object.keys(list4).sort((a, b) => list4[b] - list4[a]).slice(0, 10),
    type: 'bar'
}];

var layout4 = {
    showlegend: false
};

Plotly.newPlot('count_reactions', data4, layout4, {scrollZoom: false, responsive: true});



var list6 = JSON.parse(document.querySelector(".list6").textContent);
var data6 = [];
for (var user in list6) {
    var trace = {
        x: Object.keys(list6[user]),
        y: Object.values(list6[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data6.push(trace);
}

var layout6 = {
    showlegend: true,
    scattergap: 0.3
};

Plotly.newPlot('count_photos_per_user_per_month', data6, layout6, {scrollZoom: false, responsive: true});




list7 = JSON.parse(document.querySelector(".list7").textContent)

var data7 = [];
for (var user in list7) {
    var trace = {
        x: Object.keys(list7[user]),
        y: Object.values(list7[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data7.push(trace);
}


var layout7 = {
    showlegend: true
};

Plotly.newPlot('count_videos_per_user_per_month', data7, layout7, {scrollZoom: false, responsive: true});



list8 = JSON.parse(document.querySelector(".list8").textContent)

var data8 = [];
for (var user in list8) {
    var trace = {
        x: Object.keys(list8[user]),
        y: Object.values(list8[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data8.push(trace);
}

var layout8 = {
    showlegend: true
};

Plotly.newPlot('count_gifs_per_user_per_month', data8, layout8, {scrollZoom: false, responsive: true});



list16 = JSON.parse(document.querySelector(".list16").textContent)


var data16 = [];
for (var user in list16) {
    var trace = {
        x: Object.keys(list16[user]),
        y: Object.values(list16[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data16.push(trace);
}

var layout16 = {
    showlegend: true
};

Plotly.newPlot('count_audiofiles_per_user_per_month', data16, layout16, {scrollZoom: false, responsive: true});



list14 = JSON.parse(document.querySelector(".list14").textContent)


var data14 = [];
for (var user in list14) {
    var trace = {
        x: Object.keys(list14[user]),
        y: Object.values(list14[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data14.push(trace);
}

var layout14 = {
    showlegend: true
};

Plotly.newPlot('count_files_per_user_per_month', data14, layout14, {scrollZoom: false, responsive: true});



list15 = JSON.parse(document.querySelector(".list15").textContent)


var data15 = [];
for (var user in list15) {
    var trace = {
        x: Object.keys(list15[user]),
        y: Object.values(list15[user]),
        name: user,
        type: 'scatter',
        orientation: 'h',
        mode: 'line'
    };
    data15.push(trace);
}

var layout15 = {
    showlegend: true,
};

Plotly.newPlot('count_share_per_user_per_month', data15, layout15, {scrollZoom: false, responsive: true});



list17 = JSON.parse(document.querySelector(".list17").textContent)
const result17 = {};
for (const user in list17) {
    result17[user] = {};
  const topWords = getTopFive(list17[user]);
  topWords.forEach(word => {
    result17[user][word] = list17[user][word];
  });
}
document.querySelector('#l17').innerHTML =
    Object.keys(result17).map(user => {
        return `<div><strong>${user}</strong>: ${Object.keys(result17[user]).map(url => `${url} (${result17[user][url]})`).join(', ')}</div>`
    }).join('');



list9 = JSON.parse(document.querySelector(".list9").textContent)

var data9 = [{
    y: Object.values(list9).sort((a, b) => b - a),
    x: Object.keys(list9).sort((a, b) => list9[b] - list9[a]),
    type: 'bar'
}];


var layout9 = {
    showlegend: false
};

Plotly.newPlot('count_react_per_user', data9, layout9, {scrollZoom: false, responsive: true});



l10 = JSON.parse(document.querySelector(".list10").textContent)
const result10 = {};
for (const user in l10) {
    result10[user] = {};
  const topWords = getTopFive(l10[user]);
  topWords.forEach(word => {
    result10[user][word] = l10[user][word];
  });
}
document.querySelector('#count_react_per_user_per_reaction').innerHTML =
    Object.keys(result10).map(user => {
        return `<div><strong>${user}</strong>: ${Object.keys(result10[user]).map(word => `${getSmiley(word)} (${result10[user][word]})`).join(', ')}</div>`
    }).join('');






l5 = JSON.parse(document.querySelector(".list5").textContent)
var data5part = [];
var tabX5part = [];
var tabY5part = [];

for (var nom in l5) {
    tabX5part.push(nom);
    somme = 0;
    somme+=Object.values(l5[nom]).reduce(function(a, b) { return a + b; }, 0);
    tabY5part.push(somme);
}

data5part.push({
    labels: tabX5part,
    values: tabY5part,
    name: 'Somme des gros mots',
    type: 'pie'
});
Plotly.newPlot('badwords_list', data5part);





const result = {};
for (const user in l5) {
  result[user] = {};
  const topWords = getTopFive(l5[user]);
  topWords.forEach(word => {
    result[user][word] = l5[user][word];
  });
}
document.querySelector('#badwords_list2').innerHTML =
    Object.keys(result).map(user => {
        return `<div><strong>${user}</strong>: ${Object.keys(result[user]).map(word => `${word} (${result[user][word]})`).join(', ')}</div>`
    }).join('');




l20 = JSON.parse(document.querySelector(".list20").textContent)
document.querySelector('.list20').innerHTML =
    `<div class='text-bubble'>${l20['Message']}</div>
    <div class="text-end author"><strong>Author: ${l20['Author']}</strong>
    <sup>Reactions: ${l20['Reactions']}</sup></div>`;
    

