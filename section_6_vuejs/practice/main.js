var appHeader = {
    template: '<h1>header</h1>'
};
  
new Vue({
    el: '#app',
    components: {
        'to-do': appHeader
    }
});