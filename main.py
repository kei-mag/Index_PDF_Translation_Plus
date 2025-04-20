import os

import flet as ft

import config_copy as conf


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        selected_files.update()
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    
    def load_translators():
        component_structure = {}
        for i,e in enumerate(conf.translators):
            component_structure[e["category"]] = component_structure

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "翻訳したいPDFを選択",
                            icon=ft.icons.UPLOAD_FILE,
                            on_click=lambda _: pick_files_dialog.pick_files(
                                dialog_title="翻訳したいPDFを選択",
                                initial_directory=os.path.expanduser("~/Downloads"),
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allowed_extensions=["pdf"],
                                allow_multiple=False,
                            ),
                        ),
                        selected_files,
                    ]
                ),
                ft.Text("2. 翻訳方法を選択"),
                ft.RadioGroup(ft.Text("grp1")),
                ft.RadioGroup(ft.Text("grp2")),
                ft.RadioGroup(ft.Text("grp3")),
                ft.Radio("radio1")
            ]
        )
    )


ft.app(main)
