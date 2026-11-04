use gpui::*;

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
pub enum Orientation {
    Horizontal,
    Vertical,
}

#[derive(IntoElement)]
pub struct ResizablePanel {
    orientation: Orientation,
}

impl ResizablePanel {
    pub fn new(orientation: Orientation) -> Self {
        Self { orientation }
    }
}

impl Render for ResizablePanel {
    fn render(&mut self, _cx: &mut ViewContext<Self>) -> impl IntoElement {
        let is_horizontal = self.orientation == Orientation::Horizontal;
        div()
            .flex()
            .flex_row()
            .when(!is_horizontal, |this| this.flex_col())
            .w_full()
            .h_full()
    }
}
