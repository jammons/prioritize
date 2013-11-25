(function(){
    hero = $('form.hero-unit');
    hero.find('input[type=button]').click(function(event){
        hero.submit();
    });
})();

(function(){
    var ChooserFormView = Backbone.View.Extend({
        events: {
            "click .item": 'choose'
        },

        choose: function(event) {
            // Function submits the winner of the comparison
            // to the form URL 
            console.log('asdf');
        }
    });
    chooserFormView = new ChooserFormView();
})();
