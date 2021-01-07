# odoo-reload-translations
Reload translation files of Odoo modules.

```
git clone https://github.com/fabiomix/odoo-reload-translations.git -b 10.0 reload_translations
```

By default, Odoo only loads new translation terms and does not overwrite existing ones,
even if the PO file has changed. This was probably a design decision, made for being able to
manually change translations from the GUI without losing them with each module update.

From a developer's perspective, this is not the behavior you would expect and so
this module was born. Once installed, open **Settings > Translations > Reload translations**
and select the modules for which you want to force the reload of translation terms.

Luckily, Odoo also provides a hidden boolean option called `overwrite_existing_translations`
that you can add to your config file. If set to `True`, when updating a module
your installation will always use the translation terms present in the PO file.
