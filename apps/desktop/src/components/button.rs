use gpui::*;

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
pub enum ButtonVariant {
    Primary,
    Secondary,
    Ghost,
}

#[derive(IntoElement)]
pub struct Button {
    label: SharedString,
    variant: ButtonVariant,
}

impl Button {
    pub fn new(label: impl Into<SharedString>, variant: ButtonVariant) -> Self {
        Self {
            label: label.into(),
            variant,
        }
    }
}

impl Render for Button {
    fn render(&mut self, _cx: &mut ViewContext<Self>) -> impl IntoElement {
        div()
            .flex()
            .items_center()
            .justify_center()
            .px_3()
            .py_1_5()
            .rounded_md()
            .cursor_pointer()
            .child(self.label.clone())
    }
}
