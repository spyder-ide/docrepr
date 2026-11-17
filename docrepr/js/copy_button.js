//----------------------------------------------------------------------------
//  Copy Button
//
//  Add a [>>>] button on the top-right corner of code samples to hide
//  the >>> and ... prompts and the output and thus make the code
//  copyable.
//
//  Copyright (c) 2011, 2012 Python Software Foundation
//  Copyright (c) 2013- The Spyder Development Team and Docrepr Contributors
//
//  Taken from https://docs.python.org/_static/copybutton.js
//  Released under the PSF License: https://docs.python.org/3/license.html
//----------------------------------------------------------------------------

//============================================================================
// On DOM content loaded
//============================================================================

document.addEventListener('DOMContentLoaded', function () {
    var blocks = document.querySelectorAll('div.highlight');
    var hideText = 'Hide prompts and output';
    var showText = 'Show prompts and output';

    for (var blockIndex = 0; blockIndex < blocks.length; blockIndex++) {
        var block = blocks[blockIndex];
        if (!block.querySelector('.gp')) {
            continue;
        }

        var button = document.createElement('button');
        button.type = 'button';
        button.className = 'copybutton';
        button.textContent = '>>>';
        button.title = hideText;
        button.setAttribute('aria-label', hideText);
        button.setAttribute('aria-pressed', 'false');

        button.addEventListener('click', function () {
            var shouldHide = this.getAttribute('aria-pressed') === 'false';

            if (shouldHide) {
                this.parentNode.classList.add('prompts-hidden');
            } else {
                this.parentNode.classList.remove('prompts-hidden');
            }

            this.setAttribute('aria-pressed', String(shouldHide));
            this.setAttribute('aria-label', shouldHide ? showText : hideText);
            this.title = shouldHide ? showText : hideText;
        });

        block.insertBefore(button, block.firstChild);
    }
});
