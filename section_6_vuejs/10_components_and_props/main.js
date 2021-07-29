// var app = new Vue({
//     el : "#app",
//     data : {
//         comment : null,
//         comments : [],
//         errors : null
//     },
//     methods: {
//         onSubmit() {
//             if (this.comment){
//                 let new_comment = this.comment;
//                 this.comments.push(new_comment);
//                 this.comment = null;

//                 if (this.errors) {
//                     this.errors = null;
//                 }
//             } else {
//                 this.errors = "The comment field can't be empty!";
//             }
//         }
//     }
// })

Vue.component("comment", {
    props: {
        comment : {
            type : Object,
            required : true
        }
    },
    template: `
        <div>
            <div class="card-body">
                <p>{{ comment.username }}</p>
                <p>{{ comment.content }}</p>
            </div>
            <hr>
        </div>
    `
})

var app = new Vue({
    el : "#app",
    data : {
        comments : [
            { username : "alice", content : "first comment" },
            { username : "json", content : "second comment" },
            { username : "ironman", content : "I'm Ironman" },
            { username : "Superman", content : "Comming Soon" }
        ]
    }
})