window.addEventListener('load', () => {

    const ch_form_select = document.querySelector('#ch_form-select');
    var active_form = document.forms[ch_form_select.value + '_form'];

    active_form.style.display = 'block';

    ch_form_select.addEventListener('change', (e) => {
        let form_name = e.target.value + '_form';
        active_form.style.display = 'none';
        active_form = document.forms[form_name];
        active_form.style.display = 'block';
    });

});
