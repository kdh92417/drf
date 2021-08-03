Vue.component("to-do", {
    props : {
        tasks: {
            type : Array,
            required : true
        },
        remaining: {
            type : Number,
            required : true
        }
    },
    template : `
    <div class="container mt-2">
        <p><strong>Remaining Tasks : {{ remaining }}</strong></p>
    </div>
    `
})

var app = new Vue({
    el : '#app',
    data : {
        tasks : []
    },
    computed : {
        taskCount() {
            return this.tasks.length;
        }
    },
    methods : {
        addNewTask(new_task) {
            this.tasks.push(new_task);
        },
        removeTask(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1);
        }
    }
})

