django-files-widget
===================

Django AJAX form widgets and model fields for multiple files/images upload with progress bar

__This is currently an alpha release. Not all functionality is there, only `ImageField` and `ImagesField` have been implemented and there is not yet enough error handling.__

Features
--------

- Drag &amp; drop file uploading via AJAX
- Uploading multiple files at once
- Upload progress bar
- Four model fields with corresponding form fields and widgets: `ImagesField`, `ImageField`, `FilesField`, and `FileField`
- Image gallery widget with drag &amp; drop reordering
- File list widget with file type icons and metadata
- Integrates with Django Admin, [Grappelli](https://github.com/sehmaschine/django-grappelli), [Django Filebrowser](https://github.com/sehmaschine/django-filebrowser) and [Mezzanine](http://mezzanine.jupo.org/)

Quick Start
-----------

### Requirements ###

- Django 1.5 or later
- [sorl-thumbnail](https://github.com/sorl/sorl-thumbnail)
- [Pillow](https://github.com/python-imaging/Pillow) (or PIL)
- Unix/Linux (file saving uses `os.link()`)
- jQuery 1.7 or later
- jQuery UI
- [jQuery File Upload](https://github.com/blueimp/jQuery-File-Upload) (included)

### Install ###

    pip install git+git://github.com/TND/django-files-widget.git

### In `settings.py` ###

    INSTALLED_APPS = (
        ...,
        'sorl.thumbnail',
        'topnotchdev.files_widget',
        ...,
    )
    
    # basic settings with their defaults
    FILES_WIDGET_TEMP_DIR = 'temp/files_widget/'        # inside MEDIA_ROOT
    FILES_WIDGET_FILES_DIR = 'uploads/files_widget/'    # inside MEDIA_ROOT
    FILES_WIDGET_JQUERY_PATH = ...
    FILES_WIDGET_JQUERY_UI_PATH = ...
    THUMBNAIL_DEBUG = True # sorl-thumbnail debug

### In `urls.py` ###

    url(r'^files-widget/', include('topnotchdev.files_widget.urls')),

### In `models.py` ###

    from topnotchdev import files_widget
  
    class MyModel(models.Model):
        image = files_widget.ImageField()
        images = files_widget.ImagesField()

### Django Auth user permissions ###

    files_widget.can_upload_files

Credits
-------

- [jQuery File Upload](https://github.com/blueimp/jQuery-File-Upload/wiki/Options)
- [Tutorial on jQuery Filedrop](http://tutorialzine.com/2011/09/html5-file-upload-jquery-php/) by Martin Angelov
- [Tutorial on Django AJAX file upload](http://kuhlit.blogspot.nl/2011/04/ajax-file-uploads-and-csrf-in-django-13.html) by Alex Kuhl
- [Answer on non-Model user permissions](http://stackoverflow.com/questions/13932774/how-can-i-use-django-permissions-without-defining-a-content-type-or-model) on Stackoverflow


API Documentation
=================

(Under construction)

Navigation
----------

### Settings

- [`FILES_WIDGET_TEMP_DIR`](#FILES_WIDGET_TEMP_DIR)
- [`FILES_WIDGET_FILES_DIR`](#FILES_WIDGET_FILES_DIR)
- [`FILES_WIDGET_JQUERY_PATH`](#FILES_WIDGET_JQUERY_PATH)
- [`FILES_WIDGET_JQUERY_UI_PATH`](#FILES_WIDGET_JQUERY_UI_PATH)
- [`FILES_WIDGET_USE_FILEBROWSER`](#FILES_WIDGET_WITH_FILEBROWSER)
- [`FILES_WIDGET_FILEBROWSER_JS_PATH`](#FILES_WIDGET_FILEBROWSER_JS_PATH)
- [`FILES_WIDGET_MAX_FILESIZE`](#FILES_WIDGET_MAX_FILESIZE) (not yet implemented)
- [`FILES_WIDGET_FILE_TYPES`](#FILES_WIDGET_FILE_TYPES) (not yet implemented)
- [`FILES_WIDGET_USE_TRASH`](#FILES_WIDGET_USE_TRASH) (not yet implemented)
- [`FILES_WIDGET_TRASH_DIR`](#FILES_WIDGET_TRASH_DIR) (not yet implemented)

### Model Fields

- [`files_widget.FileField()`](#FileField) (not yet implemented)
- [`files_widget.FilesField()`](#FilesField) (not yet implemented)
- [`files_widget.ImageField()`](#ImageField)
- [`files_widget.ImagesField()`](#ImagesField)

### Model Field Options

- [`max_length`](#max_length)
- [`on_delete`](#on_delete) (not yet implemented)
- [`max_files`](#max_files) (not yet implemented)
- [`max_filesize`](#max_filesize) (not yet implemented)
- [`file_types`](#file_types) (not yet implemented)

### FilesField and ImagesField Instance Attributes

- [`splitlines()`](#splitlines)
- [`all()`](#all)
- [`next()`](#next)
- [`next_n()`](#next_n)
- [`has_next()`](#has_next)
- [`as_list()`](#as_list) (not yet implemented)
- [`as_gallery()`](#as_gallery) (not yet implemented)
- [`as_carousel()`](#as_carousel) (not yet implemented)

### FileField, FilesField, ImageField and ImagesField Instance Attributes

- [(unicode)](#unicode)
- [`escaped`](#escaped)
- [`url`](#url)
- [`local_path`](#local_path)
- [`filename`](#filename)
- [`name`](#name)
- [`ext`](#ext)
- [`img_tag()`](#img_tag)
- [`thumbnail()`](#thumbnail)
- [`thumbnail_mxn()`](#thumbnail_mxn)
- [`thumbnail_tag()`](#thumbnail_tag)
- [`thumbnail_tag_mxn()`](#thumbnail_tag_mxn)
- [`exists()`](#exists)
- [`get_size()`](#get_size)
- [`get_accessed_time()`](#get_accessed_time)
- [`get_created_time()`](#get_created_time)
- [`get_modified_time()`](#get_modified_time)

### Django Auth Permissions

- [`files_widget.can_upload_files`](#can_upload_files)
- [`files_widget.can_remove_files`](#can_remove_files) (not yet implemented)

### Static Files Inclusion

- [`form.media`](#form.media)
- [`files_widget/media.html`](#media.html) (not yet implemented)
- [Manual](#manual-inclusion)

### Signals

- [`files_widget.signals.pre_upload`](#pre_upload) (not yet implemented)
- [`files_widget.signals.post_upload`](#post_upload) (not yet implemented)
- [`files_widget.signals.pre_move`](#pre_move) (not yet implemented)
- [`files_widget.signals.post_move`](#post_move) (not yet implemented)
- [`files_widget.signals.pre_delete`](#pre_delete) (not yet implemented)
- [`files_widget.signals.post_delete`](#post_delete) (not yet implemented)

### Signal Handlers

- [`post_save`](#django.post_save)
- [`post_delete`](#django.post_delete) (not yet implemented)

### Management Commands

- [`manage.py files_widget cleanup`](#cleanup) (not yet implemented)
