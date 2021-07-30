const App = {
    data() {
        return {
            comment : null,
            comments : [],
            errors : null
        }
    },
    methods : {
        onSubmit() {
            if (this.comment) {
                new_comment = this.comment;
                this.comments.push(new_comment);
                this.comment = null;

                if (this.errors) {
                    this.errors = null;
                }
            } else {
                this.errors = "댓글의 내용을 입력해주세요"
            }
            
        }
    }
}

Vue.createApp(App).mount('#app')