import bpy

bl_info = {
    "name": "Blender Bender Watermark",
    "author": "Naimeee",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > UI > Tool > Blender Bender Watermark",
    "description": "This small addon help you create a watermark in seconds",
    "category": "Object"
}

class WatermarkOperator(bpy.types.Operator):
    bl_idname = "object.watermark_operator"
    bl_label = "Add Watermark"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        user_name = context.scene.watermark_name

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Collection set-up
        credits_collection = bpy.data.collections.new("Credits")
        bpy.context.scene.collection.children.link(credits_collection)
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["Credits"]
        
        
        # 1st text
        bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.object.editmode_toggle()
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.text_insert(text="Ported by " + user_name)
        bpy.ops.font.line_break()
        bpy.ops.font.text_insert(text="@ BlendBend")
        bpy.ops.object.editmode_toggle()
        bpy.context.object.rotation_euler[0] = 1.5708
        bpy.context.object.location[1] = 10
        bpy.context.object.location[2] = 1
        bpy.context.object.data.align_x = 'CENTER'
        bpy.data.objects["Text"].name = "ported by " + user_name + " @ BlendBend"
        bpy.context.object.hide_select = True
        bpy.context.object.hide_render = True
        
        # 2nd text
        bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.object.editmode_toggle()
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.text_insert(text="(discord.com/invite/p8VeqRtGmp)")
        bpy.ops.object.editmode_toggle()
        bpy.context.object.scale[0] = 0.5
        bpy.context.object.scale[1] = 0.5
        bpy.context.object.scale[2] = 0.5
        bpy.context.object.rotation_euler[0] = 1.5708
        bpy.context.object.location[1] = 10
        bpy.context.object.location[2] = -1
        bpy.context.object.data.align_x = 'CENTER'
        bpy.data.objects["Text"].name = "discord.com/invite/p8VeqRtGmp"
        bpy.context.object.hide_select = True
        bpy.context.object.hide_render = True
        
        return {"FINISHED"}

class WatermarkPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_watermark_panel"
    bl_label = "Blender Bender Watermark"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.prop(context.scene, "watermark_name", text="Name")
        col.operator("object.watermark_operator", text="Watermark")

def register():
    bpy.utils.register_class(WatermarkOperator)
    bpy.utils.register_class(WatermarkPanel)
    bpy.types.Scene.watermark_name = bpy.props.StringProperty(name="Name", default="")

def unregister():
    bpy.utils.unregister_class(WatermarkOperator)
    bpy.utils.unregister_class(WatermarkPanel)
    del bpy.types.Scene.watermark_name

if __name__ == "__main__":
    register()