from ui.gui.components.dialogs.success_dialog import SuccessDialog
from ui.gui.components.dialogs.error_dialog import ErrorDialog
from ui.gui.components.dialogs.warning_dialog import WarningDialog
from ui.gui.components.dialogs.confirm_dialog import ConfirmDialog


class Notification:

    @staticmethod
    def success(master, message):

        dialog = SuccessDialog(
            master,
            message
        )

        master.wait_window(dialog)

    @staticmethod
    def error(master, message):

        dialog = ErrorDialog(
            master,
            message
        )

        master.wait_window(dialog)

    @staticmethod
    def warning(master, message):

        dialog = WarningDialog(
            master,
            message
        )

        master.wait_window(dialog)

    @staticmethod
    def confirm(master, message):

        dialog = ConfirmDialog(
            master,
            message
        )

        master.wait_window(dialog)

        return dialog.result