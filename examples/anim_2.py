import lvgl as lv
import time

lv.init()
disp = lv.sdl_window_create(480, 320)
group = lv.group_create()
lv.group_set_default(group)
mouse = lv.sdl_mouse_create()
keyboard = lv.sdl_keyboard_create()
lv.indev_set_group(keyboard, group)


def anim_x(a, v):
    lv.obj_set_x(obj, v)


def anim_size(a, v):
    lv.obj_set_size(obj, v, v)


anim_x_cb = lv.anim_custom_exec_cb_t(anim_x)
anim_size_cb = lv.anim_custom_exec_cb_t(anim_size)

#
# Create a playback animation
#
obj = lv.obj_create(lv.scr_act())
lv.obj_set_style_bg_color(obj, lv.palette_main(lv.PALETTE_RED), 0)
lv.obj_set_style_radius(obj, lv.RADIUS_CIRCLE, 0)

lv.obj_align(obj, lv.ALIGN_LEFT_MID, 10, 0)
a1_ease_in_out_cb = lv.anim_path_cb_t(lv.anim_path_ease_in_out)

a1 = lv.anim_t()
lv.anim_init(a1)
lv.anim_set_var(a1, obj)
lv.anim_set_values(a1, 10, 50)
lv.anim_set_time(a1, 1000)
lv.anim_set_playback_delay(a1, 100)
lv.anim_set_playback_time(a1, 300)
lv.anim_set_repeat_delay(a1, 500)
lv.anim_set_repeat_count(a1, lv.ANIM_REPEAT_INFINITE)
lv.anim_set_path_cb(a1, a1_ease_in_out_cb, None)
lv.anim_set_custom_exec_cb(a1, anim_size_cb, None)
lv.anim_start(a1)


a2_ease_in_out_cb = lv.anim_path_cb_t(lv.anim_path_ease_in_out)


a2 = lv.anim_t()
lv.anim_init(a2)
lv.anim_set_var(a2, obj)
lv.anim_set_values(a2, 10, 240)
lv.anim_set_time(a2, 1000)
lv.anim_set_playback_delay(a2, 100)
lv.anim_set_playback_time(a2, 300)
lv.anim_set_repeat_delay(a2, 500)
lv.anim_set_repeat_count(a2, lv.ANIM_REPEAT_INFINITE)
lv.anim_set_path_cb(a2, a2_ease_in_out_cb, None)
lv.anim_set_custom_exec_cb(a2, anim_x_cb, None)
lv.anim_start(a2)


start = time.time()

while True:
    stop = time.time()
    diff = int((stop * 1000) - (start * 1000))
    if diff >= 1:
        start = stop
        lv.tick_inc(diff)
        lv.task_handler()

