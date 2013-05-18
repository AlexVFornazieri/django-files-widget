from django.conf import settings

MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
TEMP_DIR = getattr(settings, 'FILES_WIDGET_TEMP_DIR', 'temp/files_widget/')
TEMP_DIR_FORMAT = getattr(settings, 'FILES_WIDGET_TEMP_DIR_FORMAT', '%4d-%02d-%02d-%02d-%02d')
FILES_DIR = getattr(settings, 'FILES_WIDGET_FILES_DIR', 'uploads/files_widget/')
OLD_VALUE_STR = getattr(settings, 'FILES_WIDGET_OLD_VALUE_STR', 'old_%s_value')
DELETED_VALUE_STR = getattr(settings, 'FILES_WIDGET_DELETED_VALUE_STR', 'deleted_%s_value')
MOVED_VALUE_STR = getattr(settings, 'FILES_WIDGET_MOVED_VALUE_STR', 'moved_%s_value')
JQUERY_PATH = getattr(settings, 'FILES_WIDGET_JQUERY_PATH', 'mezzanine/js/jquery-1.7.1.min.js')
JQUERY_UI_PATH = getattr(settings, 'FILES_WIDGET_JQUERY_UI_PATH', 'js/jquery-ui-1.10.3.custom.js')
FILEBROWSER_JS_PATH = getattr(settings, 'FILES_WIDGET_FILEBROWSER_JS_PATH', 'filebrowser/js/AddFileBrowser.js')

if not len(MEDIA_ROOT) or not len(TEMP_DIR) or not len(FILES_DIR) or TEMP_DIR == FILES_DIR:
    raise Exception("MEDIA_ROOT, FILES_WIDGET_TEMP_DIR and FILES_WIDGET_FILES_DIR must be set and different")
