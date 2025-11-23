// static/js/main.js
document.addEventListener('DOMContentLoaded', function(){
  const form = document.getElementById('txnForm');
  form.addEventListener('submit', function(e){
    const amount = parseFloat(form.amount.value||0);
    if(isNaN(amount) || amount < 0){ e.preventDefault(); alert('Enter valid amount'); return; }
    const hour = parseInt(form.hour.value||0,10);
    if(hour<0 || hour>23){ e.preventDefault(); alert('Hour must be 0-23'); return; }
  });
});
