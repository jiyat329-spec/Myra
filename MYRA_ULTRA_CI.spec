# MYRA ULTRA — portable PyInstaller spec for GitHub Actions (Windows)
# MYRA_ULTRA.spec jaisa hi hai, bas hardcoded C:\Users\Vikas\... paths hata diye gaye hain.
# -*- mode: python ; coding: utf-8 -*-
import os
import certifi
from PyInstaller.utils.hooks import collect_submodules, collect_all

HERE = os.path.abspath(SPECPATH)


def _p(*parts):
    return os.path.join(HERE, *parts)


def _safe_collect_all(pkg):
    try:
        return collect_all(pkg)
    except Exception as e:
        print(f"[spec] skip collect_all({pkg}): {e}")
        return [], [], []


def _safe_submodules(pkg):
    try:
        return collect_submodules(pkg)
    except Exception as e:
        print(f"[spec] skip collect_submodules({pkg}): {e}")
        return []


# ── Data files (source relative to this spec, destination inside EXE) ─────────
_data_rel = [
    ('aria.py', '.'), ('aria_ui.py', '.'), ('myra_ui.py', '.'), ('myra_pages.py', '.'),
    ('myra_actions.py', '.'), ('myra_quick_features.py', '.'), ('myra_edge_glow.py', '.'),
    ('myra_float_orb.py', '.'), ('myra_guardian.py', '.'), ('myra_autostart.py', '.'),
    ('myra_prefs.py', '.'), ('myra_slot.py', '.'), ('myra_lang.py', '.'),
    ('myra_splash.py', '.'), ('myra_apps.py', '.'), ('myra_spotify.py', '.'),
    ('myra_studio.py', '.'),
    ('aria_modules', 'aria_modules'), ('myra', 'myra'),
    ('website_builder', 'website_builder'),
    ('myra_coder_integration.py', '.'), ('myra_coder', 'myra_coder'),
    ('Aria_office_manage.py', '.'), ('Main_normal.py', '.'), ('main_hotkey.py', '.'),
    ('aria_daemon.py', '.'), ('aria_startup.py', '.'),
    ('prompt.py', '.'), ('normal_prompt.py', '.'),
    ('camera_vision_module.py', '.'), ('screen_share_module.py', '.'),
    ('whatsapp_file_sender.py', '.'), ('aria_icon.ico', '.'),
    ('aria_modules/haarcascade_frontalface_default.xml', 'aria_modules'),
]

datas = []
for _src, _dst in _data_rel:
    _abs = _p(*_src.split('/'))
    if os.path.exists(_abs):
        datas.append((_abs, _dst))
    else:
        print(f"[spec] WARNING: missing data file skipped: {_src}")

datas.append((certifi.where(), 'certifi'))

# ── Binaries: PortAudio DLL (mic ke liye) ─────────────────────────────────────
binaries = []
try:
    import _sounddevice_data
    _pa_dir = os.path.join(os.path.dirname(_sounddevice_data.__file__), 'portaudio-binaries')
    if os.path.isdir(_pa_dir):
        for _f in os.listdir(_pa_dir):
            if _f.lower().endswith('.dll') and '64bit' in _f.lower():
                binaries.append((os.path.join(_pa_dir, _f), '.'))
except Exception as e:
    print(f"[spec] PortAudio DLL not found via _sounddevice_data: {e}")

hiddenimports = ['PyQt5.QtWidgets', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.sip', 'PyQt5.QtMultimedia', 'PyQt5.QtWebEngineWidgets', 'websockets', 'websockets.legacy', 'websockets.legacy.client', 'websockets.legacy.server', 'websockets.connection', 'websockets.exceptions', 'websockets.frames', 'websockets.http11', 'websockets.streams', 'websockets.uri', 'requests', 'requests.adapters', 'requests.auth', 'requests.cookies', 'requests.exceptions', 'requests.models', 'requests.sessions', 'urllib3', 'urllib3.util', 'urllib3.util.retry', 'urllib3.util.ssl_', 'certifi', 'aiohttp', 'urllib.request', 'urllib.parse', 'sounddevice', '_sounddevice_data', 'pyaudio', 'wave', 'asyncio', 'asyncio.events', 'asyncio.futures', 'asyncio.tasks', 'asyncio.streams', 'asyncio.queues', 'asyncio.locks', 'asyncio.protocols', 'asyncio.transports', 'asyncio.selector_events', 'asyncio.windows_events', 'asyncio.windows_utils', 'pyrebase', 'pyrebase.pyrebase', 'python_jwt', 'jwcrypto', 'jwcrypto.jwt', 'cryptography', 'cryptography.hazmat', 'cryptography.hazmat.primitives', 'cryptography.hazmat.primitives.asymmetric', 'cryptography.hazmat.backends', 'cryptography.hazmat.backends.openssl', 'cv2', 'numpy', 'numpy.core', 'numpy.core._multiarray_umath', 'PIL', 'PIL.Image', 'PIL.ImageDraw', 'PIL.ImageEnhance', 'PIL.ImageFilter', 'pyttsx3', 'pyttsx3.drivers', 'pyttsx3.drivers.sapi5', 'win32com.client', 'win32com.server', 'win32api', 'win32con', 'win32gui', 'win32process', 'pythoncom', 'winreg', 'comtypes', 'comtypes.client', 'winsound', 'google.genai', 'google.genai.types', 'google.generativeai', 'psutil', 'pyperclip', 'pyautogui', 'pygetwindow', 'yt_dlp', 'qrcode', 'qrcode.image', 'qrcode.image.pil', 'pywhatkit', 'duckduckgo_search', 'speedtest', 'phonenumbers', 'pypdf', 'mss', 'mss.windows', 'pynput', 'pynput.keyboard', 'pynput.mouse', 'openpyxl', 'docx', 'pptx', 'win32clipboard', 'ctypes', 'sqlite3', 'json', 'uuid', 're', 'dotenv', 'threading', 'subprocess', 'glob', 'shutil', 'tempfile', 'secrets', 'pathlib', 'datetime', 'collections', 'hashlib', 'socket', 'jaraco', 'jaraco.packaging', 'jaraco.text', 'colorama', 'ssl', 'aria_modules.license_client', 'aria_modules.aria_activation', 'aria_modules.firebase_connection', 'aria_modules.tools', 'aria_modules.cloud_database', 'aria_modules.face_auth', 'aria_modules.minibar_aria', 'aria_modules.aria_advanced_tools', 'aria_modules.aria_advanced_features', 'aria_modules.aria_login', 'aria_modules.game_install', 'myra.cli', 'myra.config', 'myra_coder_integration', 'prompt', 'normal_prompt', 'whatsapp_file_sender', 'Aria_office_manage', 'camera_vision_module', 'screen_share_module']
hiddenimports += ['rapidfuzz', 'rapidfuzz.fuzz']

for _pkg in ['websockets', 'requests', 'pywinauto', 'urllib3', 'google.genai', 'PIL', 'cv2',
             'mss', 'win32com', 'pyautogui', 'aria_modules', 'myra', 'website_builder',
             'numpy', 'asyncio']:
    hiddenimports += _safe_submodules(_pkg)

for _pkg in ['sounddevice', '_sounddevice_data', 'certifi', 'pyrebase', 'python_jwt', 'jwcrypto',
             'cryptography', 'duckduckgo_search', 'yt_dlp', 'pywhatkit', 'pyttsx3', 'jaraco',
             'aria_modules', 'website_builder']:
    _d, _b, _h = _safe_collect_all(_pkg)
    datas += _d
    binaries += _b
    hiddenimports += _h


a = Analysis(
    [_p('Main_normal.py')],
    pathex=[HERE],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[_p('admin_and_build_tools', '_aria_rthook.py')],
    excludes=['torchaudio', 'tensorflow', 'keras', 'sklearn', 'scipy', 'pandas', 'matplotlib',
              'IPython', 'notebook', 'jupyter', 'acrcloud', 'pynvml', 'PySide6', 'tkinter',
              'test', 'unittest', '_pytest', 'onnxruntime', 'onnx', 'firebase_admin',
              'google.cloud.firestore'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MYRA_ULTRA',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[_p('aria_icon.ico')],
)
