# -*- coding: utf-8 -*-
"""نقطة الدخول"""
import sys
import traceback


def main():
    try:
        from app import BaytScanOS
        app = BaytScanOS()
        app.mainloop()
    except Exception:
        traceback.print_exc()
        try:
            from tkinter import messagebox
            messagebox.showerror(
                "خطأ فادح",
                "حدث خطأ غير متوقع أثناء التشغيل.\n"
                "راجع الملفات في مجلد التطبيق.\n\n"
                + traceback.format_exc(limit=3)
            )
        except Exception:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()