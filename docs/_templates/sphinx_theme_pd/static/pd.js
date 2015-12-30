$(function () {

    var admonitions = {
        'note': 'message',
        'warning': 'warning',
        'admonition-todo': 'bookmark'
    };
    var iconSize = 'md-30';

    jQuery.each(admonitions, function (cls, text) {
        var container = $("div." + cls + " > p.admonition-title");
        container.prepend('<i class="material-icons ' + iconSize + '">' + text + '</i>')
    });

    $("a.headerlink").html('').prepend('<i class="material-icons">link</i>');

    var domain_classes = {
        'function': 'function',
        'class': 'class',
        'method': 'method',
        'staticmethod': 'staticmethod',
        'classmethod': 'classmethod'
    };

    jQuery.each(domain_classes, function (cls, text) {
        var container_dt = $("dl." + cls + " > dt");
        var container_em = $("dl." + cls + " > dt > em.property");

        if (container_em[0]) {
            // nothing to do;
        } else {
            container_dt.prepend('<em class="property">' + text + ' </em>')
        }

        container_dt.prepend('<i class="material-icons ' + iconSize + '">code</i>');
    });
});
