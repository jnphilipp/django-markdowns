# django_markdowns

Provides markdown functionality for Django via a template filter.

## Features:
 * Adding `md` Django template filter.
 * Adding `DjangoExtension` extension for markdown package.
   * use of Django URL syntax.
     ```
     [Some link](APP_NAME:VIEW_NAME|PARAMS,COMMA,SEPARATED)
     ```
