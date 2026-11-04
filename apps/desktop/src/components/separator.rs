use gpui::*;

#[derive(IntoElement)]
pub struct Separator;

impl Separator {
    pub fn new() -> Self {
        Self
    }
}

impl Render for Separator {
    fn render(&mut self, _cx: &mut ViewContext<Self>) -> impl IntoElement {
        div().w_full().h_px().bg_border()
    }
}
