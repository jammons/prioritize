(function(){
    hero = $('form.hero-unit');
    hero.find('input[type=button]').click(function(event){
        hero.submit();
    });
})();

(function(){
    var ChooserFormView = Backbone.View.extend({
        events: {
            "click": 'choose'
        },

        choose: function(event) {
            // Function submits the winner of the comparison
            // to the form URL 
            var winner_id, loser_id;

            winner_id = $(event.currentTarget).data('id');
            loser_id = $(event.currentTarget).siblings('.item').data('id');
            this.submitWinner(winner_id, loser_id);
        },

        submitWinner: function(winner_id, loser_id) {
            hero = $('.hero-unit form');
            hero.find('input[name=winner]').val(winner_id);
            hero.find('input[name=loser]').val(loser_id);
            hero.submit();
        }
    });

    $('.item').each(
        function(){
            chooserFormView = new ChooserFormView({ el: this });
    });
})();
