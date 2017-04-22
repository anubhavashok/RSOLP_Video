function lxsfile = renderLuxblend(blendfile, BLENDER_BIN, renderparams, runRenderer)        
%     %example render params:    
%     renderparams.h = 10;
%     renderparams.w = 10;
%     renderparams.halt_spp = 50;
%     renderparams.outpath = '//';

    if(~exist('runRenderer','var'))
        runRenderer = true;
    end

    %LUXCONSOLE_BIN = '/srv/rsolp/rsolp/src/luxconsole/lux-v08-x86_64-sse2-NoOpenCL/luxconsole';    
    LUXCONSOLE_BIN = '/Applications/LuxRender/LuxRender.app/Contents/MacOS/luxconsole';
    tmppy = ['.tmp-' timestamp() '.py'];
    fid = fopen(tmppy, 'w');
    fprintf(fid, 'import bpy\n');
    if(exist('renderparams', 'var'))
        fprintf(fid, 'bpy.context.scene.render.filepath = "%s"\n', renderparams.outpath);
        fprintf(fid, 'bpy.context.scene.render.resolution_x = %d\n', renderparams.w);
        fprintf(fid, 'bpy.context.scene.render.resolution_y = %d\n', renderparams.h);
        fprintf(fid, 'bpy.context.scene.luxrender_halt.haltspp = %d\n', renderparams.halt_spp);
        %fprintf(fid, 'bpy.context.scene.luxrender_halt.halttime = %d\n', 10);
    end
    fprintf(fid, 'bpy.context.scene.luxrender_engine.write_files = True\n');
    fprintf(fid, 'bpy.context.scene.luxrender_engine.render = False\n'); %= True\n');
    fprintf(fid, 'bpy.ops.render.render()\n');
    fprintf(fid, '\n');
    fclose(fid);
   
    %display(sprintf('%s -b %s -E LUXRENDER_RENDER -P %s', BLENDER_BIN, blendfile, tmppy));
    [result,foo] = system(sprintf('%s -b %s -E LUXRENDER_RENDER -P %s', BLENDER_BIN, blendfile, tmppy));
    [path, file, ext] = fileparts(blendfile);
    lxsfiles = dir(fullfile(path,'*.lxs'));
    lxsfile = fullfile(path,lxsfiles(1).name);
    if(runRenderer == true)
        %display(sprintf('%s %s', LUXCONSOLE_BIN, lxsfile));
        [result,foo] = system(sprintf('%s %s', LUXCONSOLE_BIN, lxsfile));
        %display('Done rendering');
    end
    delete(tmppy);
end
