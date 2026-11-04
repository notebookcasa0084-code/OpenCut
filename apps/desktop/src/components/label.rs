use gpui::*;

#[derive(IntoElement)]
pub struct Label {
    text: SharedString,
}

impl Label {
    pub fn new(text: impl Into<SharedString>) -> Self {
        Self {
            text: text.into(),
        }
    }
}

impl Render for Label {
    fn render(&mut self, _cx: &mut ViewContext<Self>) -> impl IntoElement {
        div().text_sm().child(self.text.clone())
    }
}
