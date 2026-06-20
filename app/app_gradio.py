import gradio as gr

from app.ml_model import predict_energy


def predict(
    YearBuilt,
    BuildingAge,
    NumberofFloors,
    Log_Surface,
    PropertyGFATotal,
    LargestPropertyUseTypeGFA,
    PropertyGFABuilding_s,
    BuildingType,
    PrimaryPropertyType,
    City,
    State,
):

    features = {
        "YearBuilt": YearBuilt,
        "BuildingAge": BuildingAge,
        "NumberofFloors": NumberofFloors,
        "Log_Surface": Log_Surface,
        "PropertyGFATotal": PropertyGFATotal,
        "LargestPropertyUseTypeGFA": LargestPropertyUseTypeGFA,
        "PropertyGFABuilding_s": PropertyGFABuilding_s,
        "BuildingType": BuildingType,
        "PrimaryPropertyType": PrimaryPropertyType,
        "City": City,
        "State": State,
    }

    prediction = predict_energy(features)

    return round(prediction, 2)


gradio_interface = gr.Interface(

    fn=predict,

    title="🏢 Seattle Energy Prediction",

    description="""
    Estimation de la consommation énergétique d'un bâtiment
    à partir de ses caractéristiques.
    """,

    inputs=[

        gr.Number(
            label="Année de construction"
        ),

        gr.Number(
            label="Âge du bâtiment"
        ),

        gr.Number(
            label="Nombre d'étages"
        ),

        gr.Number(
            label="Log Surface"
        ),

        gr.Number(
            label="Surface totale (sq ft)"
        ),

        gr.Number(
            label="Largest Property Use Type GFA"
        ),

        gr.Number(
            label="Property GFA Building"
        ),

        gr.Dropdown(

            choices=[
                "Campus",
                "NonResidential",
                "Multifamily"
            ],

            label="Type de bâtiment"
        ),

        gr.Textbox(
            label="Type principal de propriété"
        ),

        gr.Textbox(
            value="Seattle",
            label="Ville"
        ),

        gr.Textbox(
            value="WA",
            label="État"
        ),

    ],

    outputs=gr.Number(
        label="Prédiction (kBtu)"
    ),

    flagging_mode="never",

    submit_btn="Prédire",

    clear_btn="Réinitialiser",
)