// Comment List Component
Vue.component('comment-list', {
    props : {
        comments : {
            type : Array,
            required : true
        }
    },
    data : function() {
        return {
            new_comment : null,
            comment_author : null,
            error : null
        }
    },
    methods : {
        submitComment(){
            if (this.new_comment && this.comment_author) {
                this.$emit('submit-comment', { username: this.comment_author,
                                               content : this.new_comment});
                this.new_comment = null;
                this.comment_author = null;
                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "모든 필드값을 입력해주세요."
            }
        }
    },
    template : `
    <div class="mb-2">
        <div class="container">

            <single-comment
                v-for="(comment, index) in comments"
                :comment="comment"
                :key="index"
            ></single-comment>

            <hr>

            <h3>{{ error }}</h3>

            <form @submit.prevent="submitComment" class="mb-4">
                <div class="form-group">
                    <label for="commentAuthor">Your Username</label>
                    <input class="form-control" 
                        type="text"
                        id="commentAuthor"
                        v-model="comment_author">
                </div>
                    
                <div class="form-group">
                    <label for="commentAuthor">Add a comment</label>
                    <textarea class="form-control" 
                            id="commentText"
                            cols="30" rows="3"
                            v-model="new_comment">
                    </textarea>
                </div>

                <button type="submit"
                        class="btn btn-sm btn-primary"
                        >Publish
                </button>
            </form>
        </div>
    </div>
    `
})


// Single Component
Vue.component('single-comment', {
    props : {
        comment : {
            type : Object,
            required : true
        }
    },
    template : `
    <div class="mb-2">
        <div class="card">
            <div class="card-header">
                <p>Published by : {{ comment.username }}</p>
            </div class="card-body">
                <p>{{ comment.content }}</p>
        </div>
    </div>
    `
})

var app = new Vue({
    el : '#app',
    data : {
        comments : [
            { username : 'adam', content : 'Hello'},
            { username : 'eve', content : 'Nice to Meet you'},
            { username : 'noa', content : 'Cut through the sea'},
            { username : 'God', content : 'God bless you'},
        ]
    },
    methods : {
        addNewComment(new_comment) {
            this.comments.push(new_comment);
        }
    }
})