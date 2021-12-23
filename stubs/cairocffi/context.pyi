from typing import Any, Optional

class Context:
    def __init__(self, target: Any) -> None: ...
    def get_target(self): ...
    def save(self) -> None: ...
    def restore(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def push_group(self) -> None: ...
    def push_group_with_content(self, content: Any) -> None: ...
    def pop_group(self): ...
    def pop_group_to_source(self) -> None: ...
    def get_group_target(self): ...
    def set_source_rgba(self, red: float, green: float, blue: float, alpha: float = ...) -> None: ...
    def set_source_rgb(self, red: float, green: float, blue: float) -> None: ...
    def set_source_surface(self, surface: Any, x: int = ..., y: int = ...) -> None: ...
    def set_source(self, source: Any) -> None: ...
    def get_source(self): ...
    def set_antialias(self, antialias: Any) -> None: ...
    def get_antialias(self): ...
    def set_dash(self, dashes: Any, offset: int = ...) -> None: ...
    def get_dash(self): ...
    def get_dash_count(self): ...
    def set_fill_rule(self, fill_rule: Any) -> None: ...
    def get_fill_rule(self): ...
    def set_line_cap(self, line_cap: Any) -> None: ...
    def get_line_cap(self): ...
    def set_line_join(self, line_join: Any) -> None: ...
    def get_line_join(self): ...
    def set_line_width(self, width: Any) -> None: ...
    def get_line_width(self): ...
    def set_miter_limit(self, limit: Any) -> None: ...
    def get_miter_limit(self): ...
    def set_operator(self, operator: Any) -> None: ...
    def get_operator(self): ...
    def set_tolerance(self, tolerance: Any) -> None: ...
    def get_tolerance(self): ...
    def translate(self, tx: Any, ty: Any) -> None: ...
    def scale(self, sx: Any, sy: Optional[Any] = ...) -> None: ...
    def rotate(self, radians: Any) -> None: ...
    def transform(self, matrix: Any) -> None: ...
    def set_matrix(self, matrix: Any) -> None: ...
    def get_matrix(self): ...
    def identity_matrix(self) -> None: ...
    def user_to_device(self, x: Any, y: Any): ...
    def user_to_device_distance(self, dx: Any, dy: Any): ...
    def device_to_user(self, x: Any, y: Any): ...
    def device_to_user_distance(self, dx: Any, dy: Any): ...
    def has_current_point(self): ...
    def get_current_point(self): ...
    def new_path(self) -> None: ...
    def new_sub_path(self) -> None: ...
    def move_to(self, x: Any, y: Any) -> None: ...
    def rel_move_to(self, dx: Any, dy: Any) -> None: ...
    def line_to(self, x: Any, y: Any) -> None: ...
    def rel_line_to(self, dx: Any, dy: Any) -> None: ...
    def rectangle(self, x: Any, y: Any, width: Any, height: Any) -> None: ...
    def arc(self, xc: Any, yc: Any, radius: Any, angle1: Any, angle2: Any) -> None: ...
    def arc_negative(self, xc: Any, yc: Any, radius: Any, angle1: Any, angle2: Any) -> None: ...
    def curve_to(self, x1: Any, y1: Any, x2: Any, y2: Any, x3: Any, y3: Any) -> None: ...
    def rel_curve_to(self, dx1: Any, dy1: Any, dx2: Any, dy2: Any, dx3: Any, dy3: Any) -> None: ...
    def text_path(self, text: Any) -> None: ...
    def glyph_path(self, glyphs: Any) -> None: ...
    def close_path(self) -> None: ...
    def copy_path(self): ...
    def copy_path_flat(self): ...
    def append_path(self, path: Any) -> None: ...
    def path_extents(self): ...
    def paint(self) -> None: ...
    def paint_with_alpha(self, alpha: Any) -> None: ...
    def mask(self, pattern: Any) -> None: ...
    def mask_surface(self, surface: Any, surface_x: int = ..., surface_y: int = ...) -> None: ...
    def fill(self) -> None: ...
    def fill_preserve(self) -> None: ...
    def fill_extents(self): ...
    def in_fill(self, x: Any, y: Any): ...
    def stroke(self) -> None: ...
    def stroke_preserve(self) -> None: ...
    def stroke_extents(self): ...
    def in_stroke(self, x: Any, y: Any): ...
    def clip(self) -> None: ...
    def clip_preserve(self) -> None: ...
    def clip_extents(self): ...
    def copy_clip_rectangle_list(self): ...
    def in_clip(self, x: Any, y: Any): ...
    def reset_clip(self) -> None: ...
    def select_font_face(self, family: str = ..., slant: Any = ..., weight: Any = ...) -> None: ...
    def set_font_face(self, font_face: Any) -> None: ...
    def get_font_face(self): ...
    def set_font_size(self, size: Any) -> None: ...
    def set_font_matrix(self, matrix: Any) -> None: ...
    def get_font_matrix(self): ...
    def set_font_options(self, font_options: Any) -> None: ...
    def get_font_options(self): ...
    def set_scaled_font(self, scaled_font: Any) -> None: ...
    def get_scaled_font(self): ...
    def font_extents(self): ...
    def text_extents(self, text: Any): ...
    def glyph_extents(self, glyphs: Any): ...
    def show_text(self, text: Any) -> None: ...
    def show_glyphs(self, glyphs: Any) -> None: ...
    def show_text_glyphs(self, text: Any, glyphs: Any, clusters: Any, cluster_flags: int = ...) -> None: ...
    def show_page(self) -> None: ...
    def copy_page(self) -> None: ...
    def tag_begin(self, tag_name: Any, attributes: Optional[Any] = ...) -> None: ...
    def tag_end(self, tag_name: Any) -> None: ...
