use gpui::*;

#[derive(IntoElement)]
pub struct Badge {
    text: SharedString,
    variant: BadgeVariant,
}

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
pub enum BadgeVariant {
    Primary,
    Secondary,
    Outline,
}

impl Badge {
    pub fn new(text: impl Into<SharedString>, variant: BadgeVariant) -> Self {
        Self {
            text: text.into(),
            variant,
        }
    }
}

impl Render for Badge {
    fn render(&mut self, _cx: &mut ViewContext<Self>) -> impl IntoElement {
        div().flex().items_center().px_2().py_1().rounded_md().child(self.text.clone())
    }
}
