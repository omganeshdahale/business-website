window.onload = () => {
    CONFIG = [
        {
            'form': document.forms['ch_form'],
            'trigger_fields': [document.querySelector('#ch_form-select')]
        },
    ];

    for (let i of CONFIG){
        for (let j of i.trigger_fields){
            j.addEventListener('change', (e) => {
                i.form.submit();
            });
        }
    }
}
