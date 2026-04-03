[app]

title = Inventaire Biodiversite

package.name = biodiversite

package.domain = org.moctar

source.dir = .

source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[app:android]

android.api = 33

android.minapi = 21

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


[app:android:debug]

android.debug = True
