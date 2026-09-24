//----------------------------------------------------------------------------
//  Math configuration options and hacks.
//
//  Copyright (c) 2013- The Spyder Development Team and Docrepr Contributors
//
//  Distributed under the terms of the MIT License.
//----------------------------------------------------------------------------

// NOTE: The MathJax configuration itself now lives inline in rich_repr.html
// (the ``window.MathJax`` object), following the MathJax 3 loading model. This
// file only keeps the small, engine-agnostic tweaks that need jQuery.

//============================================================================
// On document ready
//============================================================================

$(document).ready(function () {
    {% if not math_on %}
    // Math rendering is disabled: show any math in monospace so it is still
    // legible as plain TeX.
    $('.math').css('font-family', 'monospace');
    {% endif %}
});
