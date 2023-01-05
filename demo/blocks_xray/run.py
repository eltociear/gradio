import gradio as gr
import random
import time

# 1. Default
# theme = gr.themes.Default()

# 2. Solid
theme = gr.themes.Solid()

# 3. Custom
# theme = gr.themes.DefaultTheme()
# theme.primary_color = "#ff0000"


def xray_model(diseases, img):
    time.sleep(4)
    return [{disease: random.random() for disease in diseases}]


def ct_model(diseases, img):
    time.sleep(3)
    return [{disease: 0.1 for disease in diseases}]

with gr.Blocks(theme=theme) as demo:
    gr.Markdown(
        """
# Detect Disease From Scan
With this model you can lorem ipsum
- ipsum 1
- ipsum 2
"""
    )
    disease = gr.CheckboxGroup(
        choices=["Covid", "Malaria", "Lung Cancer"], label="Disease to Scan For"
    )

    with gr.Tab("X-ray") as x_tab:
        with gr.Row():
            xray_scan = gr.Image()
            xray_results = gr.JSON()
        xray_run = gr.Button("Run", variant="primary")
        xray_run.click(
            xray_model,
            inputs=[disease, xray_scan],
            outputs=xray_results,
            api_name="xray_model"
        )

    with gr.Tab("CT Scan"):
        with gr.Row():
            ct_scan = gr.Image()
            ct_results = gr.JSON()
        ct_run = gr.Button("Run")
        ct_run.click(
            ct_model,
            inputs=[disease, ct_scan],
            outputs=ct_results,
            api_name="ct_model"
        )

    upload_btn = gr.Button("Upload Results")
    upload_btn.click(
        lambda ct, xr: time.sleep(5),
        inputs=[ct_results, xray_results],
        outputs=[],
    )

if __name__ == "__main__":
    demo.launch()
